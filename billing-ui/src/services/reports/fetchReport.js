/*
 * Copyright 2020(c) The Ontario Institute for Cancer Research. All rights reserved.
 *
 * This program and the accompanying materials are made available under the terms of the GNU Public
 * License v3.0. You should have received a copy of the GNU General Public License along with this
 * program. If not, see <http://www.gnu.org/licenses/>.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
 * FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
 * WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
import { map } from 'lodash';
import encodeUriSegment from 'encode-uri-query';
import fetchHeaders from '../../utils/fetchHeaders';
import user from '../../user';

async function fetchReport({
    bucketSize, fromDate, projects, toDate,
}) {
    const query = map({
        bucket: bucketSize,
        fromDate,
        toDate,
        ...(projects.length ? { projects: projects.map(p => p.id).join(',') } : {}),
    }, (value, key) => `${key}=${encodeUriSegment(value)}`).join('&');

    const response = await fetch(`/api/reports?${query}`, {
        headers: fetchHeaders.get(),
        method: 'GET',
    });

    user.token = response.headers.get('authorization');

    return ([200].includes(response.status))
        ? Promise.resolve(response.json())
        : (
            [401, 404].includes(response.status) && user.logout(),
            Promise.reject(response)
        );
}

export default fetchReport;
